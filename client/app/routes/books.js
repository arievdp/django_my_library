import Route from '@ember/routing/route';
import Store from '@ember-data/store';

export default class BooksRoute extends Route {

  model() {
    const store = this.get('store');
    return store.findAll('book');
  }
}
